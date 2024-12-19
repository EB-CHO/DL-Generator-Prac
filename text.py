import os
import streamlit as st

# Streamlit secrets
USER_ID = st.secrets["USER_ID"]
PAT = st.secrets["PAT"]
APP_ID = st.secrets["APP_ID"]
WORKFLOW_ID_TEXT = st.secrets["WORKFLOW_ID_TEXT"]

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

@st.cache_data(persist=True)
def generate_story_from_text(user_input):

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (("authorization", "Key " + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_workflow_results_response = stub.PostWorkflowResults(
        service_pb2.PostWorkflowResultsRequest(
            user_app_id=userDataObject,  
            workflow_id=WORKFLOW_ID_TEXT,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw = user_input
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
        print(post_workflow_results_response.status)
        raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

    results = post_workflow_results_response.results[0]

    return results.outputs[1].data.text.raw

# text.py 또는 image.py의 함수 내부
print(post_workflow_results_response)  # 전체 응답 확인
print(post_workflow_results_response.status)  # 상태 확인
print(post_workflow_results_response.results)  # 결과 데이터 확인
