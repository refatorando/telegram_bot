import crypto

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("oi", "ola", "olá"):
        return "E ai, blz?"
    elif "canal" in user_message:
        return "Refatorando: https://youtube.com/refatorando \n            Inscreva-se ☝️"
    elif "crypto update" in user_message:
        return crypto.get_all()
    elif "crypto" in user_message:
        return crypto.get_info(user_message.split(" ")[1].upper())

    return "não estou entendendo você! tente novamente."