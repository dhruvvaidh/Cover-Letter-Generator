import streamlit as st
from langchain.chains.llm import LLMChain
from llm import create_output_chain,create_prompt_template


def main():
    st.title("Cover Letter Generator")
    st.subheader("Enter your profile")
    with st.form("Input"):
        job_title = st.text_input("Enter your Job Title: ")
        job_description = st.text_input("Preferred Qualifications:")
        company_name = st.text_input("Hiring Company:")
        name = st.text_input("Applicant Name:")
        prev_work_ex = st.text_input("Previous Work Experience: ")
        cur_work_ex = st.text_input("Current Work Experience: ")
        qualifications = st.text_input("Qualifications: ")
        skillsets = st.text_input("Skillsets: ")
        submitted = st.form_submit_button("Generate")
    
    if submitted:
        input = 'Job Title: ' + job_title +'\n'+ 'Preferred Qualifications: \n'+job_description +'\n'+ 'Hiring Company: \n'+company_name +'\n'+ 'Applicant Name: \n'+name +'\n'+'Working Experience: ' +prev_work_ex + ' \n'+ cur_work_ex +'\n'+ 'Qualifications: '+qualifications +'\n'+ 'Skillsets: \n'+skillsets
        prompt = create_prompt_template(input)
        chain = create_output_chain(prompt)
        result = chain.run()

    if result:
        st.subheader("Cover Letter: ")
        st.text(result)

if __name__ == "__main__":
    main()