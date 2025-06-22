from llm_helper import llm
from few_shot import FewShotPosts



few_shot = FewShotPosts()
def get_length_str(length):
    if length == "Short":
        return "5 to 10 lines"
    if length == "Medium":
        return "11 to 20 lines"
    if length == "Long":
        return "21 to 30 lines"



def get_prompt(lenght, language, topic, influencer):
    lenght_str = get_length_str(lenght)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {topic}
    2) Length: {lenght_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    examples = few_shot.get_filtered_posts(lenght, language, topic, influencer)
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following example"
        for i, post in enumerate(examples):
            post_text = post["text"]
            prompt += f"\n\n Example {i+1} \n\n {post_text}"
            if i == 2:
                break
    return prompt


def generate_post(lenght, language, topic, influencer):
    
    prompt = get_prompt(lenght, language, topic, influencer)
    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    post = generate_post("Medium", "English", "Mental Health", "ClementDelangue")
    print(post)
