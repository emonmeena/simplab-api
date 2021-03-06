from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import numpy as np

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
from django.conf import settings


def PDFgenerator(
    assignment_id,
    exp_name,
    exp_aim,
    exp_procedure,
    exp_obs,
    exp_res,
    st_name,
    st_email,
    sub_id,
):
    final_sub_path = (
        "./media/submission_files/" + st_name + "_Assignment-{}.pdf".format(sub_id)
    )
    doc = SimpleDocTemplate(
        final_sub_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))

    ptext = '<font size="20">Assignment - {} {}</font>'.format(assignment_id, exp_name)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">Student Name- %s</font>' % st_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    ptext = '<font size="12">Student Email - %s</font>' % st_email
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = '<font size="16">Aim</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">%s</font>' % exp_aim
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = '<font size="16">Procedure</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # for x in exp_procedure:
    #     ptext = '<font size="12">%s</font>' % x
    #     Story.append(Paragraph(ptext, styles["Normal"]))
    #     Story.append(Spacer(1, 12))

    ptext = '<font size="12">%s</font>' % exp_procedure
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))    

    ptext = '<font size="16">Observation</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">{}</font>'.format(exp_obs)
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = '<font size="16">Result</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size="12">{}</font>'.format(exp_res)
    Story.append(Paragraph(ptext, styles["Normal"]))

    doc.build(Story)


@api_view(["GET"])
def get_user(request, userid):
    if request.method == "GET":
        users = User_Detail.objects.get(user=userid)
        serializedData = User_Detail_Serializer(users)
        return Response(serializedData.data)


@api_view(["POST", "GET"])
def post_user(request):
    if request.method == "GET":
        users = User_Detail.objects.all()
        serializedData = User_Detail_Serializer(users, many=True)
        return Response(serializedData.data)

    if request.method == "POST":
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            serialized_user_detail = User_Detail_Serializer(
                data={
                    "user": serialized_user.data["id"],
                    "username": request.data["username"],
                    "email": request.data["email"],
                }
            )
            if serialized_user_detail.is_valid():
                serialized_user_detail.save()
            return Response(serialized_user.data["id"])
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def auth_user(request, username, password):
    try:
        user = User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        user_detail = User_Detail.objects.get(user=user.id)
        serializedData = User_Detail_Serializer(user_detail)
        return Response(serializedData.data)


@api_view(["GET"])
def get_simulations(request):
    if request.method == "GET":
        simulations = Experiment.objects.all()
        serializedData = Experimennt_Serializer(simulations, many=True)
        return Response(serializedData.data)


@api_view(["GET"])
def get_exp_detail(request, exp_id):
    try:
        exp = Experiment.objects.get(pk=exp_id)
    except Experiment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializedData = Experimennt_Serializer(exp)
        return Response(serializedData.data)


@api_view(["POST"])
def post_assignment(request):
    if request.method == "POST":
        serialized_assignment = Assignment_Serializer(data=request.data)
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST", "GET"])
def post_team(request):
    if request.method == "GET":
        teams = Team.objects.all()
        serializedData = Team_Serializer(teams, many=True)
        return Response(serializedData.data)

    if request.method == "POST":
        serialized_team = Team_Serializer(data=request.data)
        if serialized_team.is_valid():
            serialized_team.save()
            return Response(serialized_team.data["id"])
        return Response(serialized_team.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def join_team(request, team_id, user_id):
    try:
        team = Team.objects.get(pk=team_id)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        team.students.add(user)
        team.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def update_password(request, user_id, password):
    try:
        user = User.objects.get(pk=user_id, password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_user = User_Serializer(user, data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serialized_user.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_team_detail(request, team_id):
    if request.method == "GET":
        team = Team.objects.get(pk=team_id)
        serializedData = Team_Serializer(team)
        return Response(serializedData.data)


@api_view(["GET"])
def get_user_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        member_teams = Team_Serializer_Basic(
            user.all_member_teams.all(), many=True
        ).data
        admin_teams = Team_Serializer_Basic(user.team_set.all(), many=True).data
        all_teams = np.concatenate((np.array(admin_teams), np.array(member_teams)))
        return Response(all_teams)


@api_view(["GET"])
def get_user_admin_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        teams = user.team_set.all()
        serializedData = Team_Serializer_Basic(teams, many=True)
        return Response(serializedData.data)


@api_view(["GET"])
def get_student_list(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        student_ids = team.students.all()
        array = []
        for x in student_ids:
            student = User_Detail.objects.get(user=x.id)
            serialized_student = User_Detail_Serializer_Basic(student)
            array.append(serialized_student.data)

        return Response(array)


@api_view(["GET"])
def get_all_team_assignments(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        assignments = team.all_team_experiments.all().order_by("due_date", "due_time")
        serializedData = Assignment_Serializer(assignments, many=True)
        return Response(serializedData.data)


@api_view(["PUT"])
def put_user_detail(request, user_id):
    try:
        user_detail = User_Detail.objects.get(user=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_user_detail = User_Detail_Serializer(user_detail, data=request.data)
        if serialized_user_detail.is_valid():
            serialized_user_detail.save()
            return Response(serialized_user_detail.data)
        return Response(
            serialized_user_detail.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def get_all_assignments(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        member_teams = user.all_member_teams.all()
        admin_teams = user.team_set.all()
        all_assignments = []
        for x in member_teams:
            s = Assignment_Serializer(
                x.all_team_experiments.all().order_by("due_date", "due_time"), many=True
            )
            for a in s.data:
                all_assignments.append(a)
        for x in admin_teams:
            s = Assignment_Serializer(
                x.all_team_experiments.all().order_by("due_date", "due_time"), many=True
            )
            for a in s.data:
                all_assignments.append(a)
        return Response(all_assignments)


@api_view(["GET"])
def getchat(request, teamid):
    try:
        team = Team.objects.get(pk=teamid)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        chats = team.chat_set.all().order_by("date", "sent_time")
        serializedData = Chat_Serializer(chats, many=True)
        return Response(serializedData.data)


@api_view(["POST"])
def post_chat(request):
    if request.method == "POST":
        serialized_chat = Chat_Serializer(data=request.data)
        if serialized_chat.is_valid():
            serialized_chat.save()
            return Response(serialized_chat.data["chat_file"])
        return Response(serialized_chat.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_team(request, teamid):
    try:
        team = Team.objects.get(pk=teamid)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        team.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def leave_team(request, teamid, userid):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User.objects.get(pk=userid)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        if user in team.students.all():
            team.students.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def add_member(request, teamid, user_email):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User_Detail.objects.get(email=user_email)
        except User_Detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        student = User.objects.get(pk=user.pk)
        team.students.add(student)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def put_assignment_detail(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_assignment = Assignment_Serializer(
            assignment, data=request.data, partial=True
        )
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(serialized_assignment.data)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def create_assignment(request):
    if request.method == "POST":
        serialized_assignment = Assignment_Serializer(data=request.data)
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def post_submission(request):
    if request.method == "POST":
        serialized_submission = Ass_Submission_Serializer(data=request.data)
        if serialized_submission.is_valid():
            serialized_submission.save()
            try:
                exp_obs = serialized_submission.data["exp_obs"]
                ass_id = serialized_submission.data["assignment"]
                exp_result = serialized_submission.data["exp_result"]
                student_name = serialized_submission.data["student_name"]
                student_email = serialized_submission.data["student_email"]
                sub_id = serialized_submission.data["id"]
                sub = AssignmentSubmission.objects.get(id=sub_id)
                ass = Assignment.objects.get(pk=ass_id)
                exp_num = ass.exp.id
                print(exp_num)
                exp = Experiment.objects.get(pk=exp_num)
                PDFgenerator(
                    exp_num,
                    exp.exp_name,
                    exp.aim,
                    exp.procedure,
                    exp_obs,
                    exp_result,
                    student_name,
                    student_email,
                    sub_id,
                )
                sub.submission_file = (
                    "/submission_files/"
                    + student_name
                    + "_Assignment-{}.pdf".format(sub_id)
                )
                sub.save()
                print(sub.submission_file, "THis is sub")
            except AssignmentSubmission.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_submission.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def submission_list(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        assignment_submissions = assignment.assignmentsubmission_set.all()
        serializedData = Ass_Submission_Serializer(assignment_submissions, many=True)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_chat_files(request, teamid):
    if request.method == "GET":
        chat_files = Chat.objects.filter(team_id=teamid, is_file=True)
        serializedData = Chat_File_Serializer(chat_files, many=True)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def leave_member(request, teamid, user_name):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        if user in team.students.all():
            team.students.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_assignment_detail(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializedData = Assignment_Serializer(assignment)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
