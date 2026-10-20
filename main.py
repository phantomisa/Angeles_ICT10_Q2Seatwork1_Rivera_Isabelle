from pyscript import document

club_members = [
    "Brixen Rabacca",
    "Zyren Jake Naguit",
    "Miko Sebastian Alvis",
    "Kristoff Lucas Dotado",
    "Sean Derrick Yeung",
    "RK Manalansan"
]

def check_membership(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    
    full_name = f"{first_name} {last_name}".strip().title()

    is_member = full_name in club_members

    messages = {
        True: f"congrats {full_name}!! you are part of the ICT club :D",
        False: f"sorry {full_name}, your name is not on the list :(("
    }

    message = messages[is_member]
    document.getElementById("result_message").innerHTML = message