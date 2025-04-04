from timeit import default_timer as timer

# Store interview data 
interview_data = []

# Set thresholds - my criteria based on how fast I think they should answer
THRESHOLDS = {
    "name": 30,        # >30s: Likely stepped away
    "job": 30,         # >30s: Hesitation (embarrassed or lying)
    "years": 5,       # >30s: Possibly lying
    "reference": 45,   # >45s: Possibly lying
    "skills": 150,     # >150s: Thinking too hard, probably exaggerating
    "qualities": 150,  # >150s: Not very unique
    "weaknesses": 150, # >150s: Fabricating weaknesses
    "achievement": 150,# >150s: Fabricating or exaggerating
    "why": 120,        # >120s: Not sure if they want the job
    "what": 150        # >150s: Nothing separates them
}

# Function to analyze response time and generate assumptions 
def analyze_response(questionList, response_time):
    if questionList in THRESHOLDS:
        threshold = THRESHOLDS[questionList]
        if response_time >= threshold:
            # Assumptions based on question 
            assumptions = {
                "name": "Likely stepped away.",
                "job": "Possible hesitation—either embarrassed or unsure about the job.",
                "years": "Possible dishonesty about work experience.",
                "reference": "Might be fabricating how they heard about the job.",
                "skills": "Thinking too hard—possibly exaggerating skills.",
                "qualities": "Took too long—might not be very unique.",
                "weaknesses": "Possible fabrication of weaknesses.",
                "achievement": "Possible exaggeration of accomplishment.",
                "why": "Uncertain about wanting the job.",
                "what": "Nothing truly separates them from others."
            }
            return assumptions.get(questionList, None)  # Returns assumption, if applicable
    return None  # Returns nothing if no assumption should be made

# Function to ask a question, track response time, and analyze individual response
def askQuestion(questionList, question_text, whatToPrint):
    start_time = timer()
    print(question_text)
    user_response = input()  
    end_time = timer()

    response_time = end_time - start_time
    assumption = analyze_response(questionList, response_time)

    # Store the response in the interview_data list
    interview_data.append({
        "question": question_text,
        "response": user_response,
        "response_time": response_time,
        "assumption": assumption
    })

    print(f"{whatToPrint}: {user_response}")
    print(f"Response Time: {response_time:.0f} seconds")

    # Print analysis only if response time exceeds the threshold
    if assumption:
        print(f"Analysis: {assumption}\n")

# List of interview questions with their criteria
questions = [ 
    {"key": "name", "text": "Please enter your name:", "print": "Welcome"},
    {"key": "job", "text": "Please enter your current occupation:", "print": "Current Job"},
    {"key": "years", "text": "How many years have you been at that job?", "print": "Years"},
    {"key": "reference", "text": "How did you hear about this job?", "print": "How interviewee heard of job"},
    {"key": "skills", "text": "What skills do you have?", "print": "Skills:"},
    {"key": "qualities", "text": "List some qualities about yourself?", "print": "Qualities of interviewee"},
    {"key": "weaknesses", "text": "What are your weaknesses?", "print": "Interviewee's Weaknesses"},
    {"key": "achievement", "text": "What is your greatest accomplishment?", "print": "Greatest Accomplishment"},
    {"key": "why", "text": "Why do you want this job?", "print": "Why interviewee wants the job"},
    {"key": "what", "text": "What separates you? Why should I hire you?", "print": "Why the interviewee feels they should be hired"}
]

# Ask all questions
for q in questions:
    askQuestion(q["key"], q["text"], q["print"])

# Function to calculate overall statistics
def analyze_overall_data():
    response_times = [entry["response_time"] for entry in interview_data]
    if response_times:
        avg_time = sum(response_times) / len(response_times)
        max_time = max(response_times)
        min_time = min(response_times)
        print("\n### Overall Analysis ###")
        print(f"Average Response Time: {avg_time:.2f} seconds")
        print(f"Fastest Response Time: {min_time:.2f} seconds")
        print(f"Slowest Response Time: {max_time:.2f} seconds")

        # Print only assumptions that exist (skip responses below threshold)
        assumptions_to_print = [entry for entry in interview_data if entry["assumption"]]

        if assumptions_to_print:
            print("\n### Individual Assumptions ###")
            for entry in assumptions_to_print:
                print(f"Question: {entry['question']}")
                print(f"Response Time: {entry['response_time']:.2f} seconds")
                print(f"Assumption: {entry['assumption']}\n")

# Run overall analysis after interview
analyze_overall_data()
