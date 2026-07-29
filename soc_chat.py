import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.1"



def ask_soc(question):

    prompt = f"""
You are an AI SOC Analyst.

Analyze the cybersecurity request below.

Provide:

1. Threat classification
2. Risk level (LOW/MEDIUM/HIGH)
3. Possible attack technique
4. MITRE ATT&CK mapping if possible
5. Investigation steps
6. Recommended response actions

Be professional and concise.

Alert or Question:

{question}
"""


    try:

        response = requests.post(

            OLLAMA_URL,

            json={

                "model": MODEL,

                "prompt": prompt,

                "stream": False

            },

            timeout=120

        )


        if response.status_code == 200:

            data = response.json()

            return data.get(
                "response",
                "No response generated"
            )


        return f"Ollama Error: {response.text}"


    except requests.exceptions.ConnectionError:

        return (
            "❌ Cannot connect to Ollama.\n\n"
            "Make sure Ollama is running:\n"
            "ollama.exe serve"
        )


    except Exception as e:

        return f"AI Error: {str(e)}"