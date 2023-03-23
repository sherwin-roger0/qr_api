import streamlit as st
import redis

if 's' not in st.session_state:
        st.session_state.s = 0

ans=[]

r = redis.Redis(
        host='redis-11153.c10.us-east-1-2.ec2.cloud.redislabs.com',
        port=11153,
        password='5Ix3uD4BdegLaMenxOooa2GJsaatJjdU')


def quiz():

    l=["Your name?","Your Age?","Male or Female?"]
    r.set("check","false")

    st.title('Grootus')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    st.write(l[st.session_state.count])
    inp=st.text_input("")

    increment = st.button('next')

    if(st.session_state.count==0):
        st.session_state.count=1

    if increment:
        if(st.session_state.count==2):
            st.session_state.s=1
        else:
            st.session_state.count += 1
            ans.append(inp)


if(not st.session_state.s):
    quiz()
else:
    st.header("Thanks for ur response")
    button=st.button("submit")
    if(button):
        r.set("check","True")
