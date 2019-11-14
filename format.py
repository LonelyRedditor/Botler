import json
import requests
import time

TOKEN = "740311034:AAFmbr6DNptB3QRS7YIwt1DYe_joblm9ZsY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
chat_id = -1001301223758

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def lock():
    url = URL + 'setChatPermissions?chat_id='+str(chat_id)+'&permissions={"can_send_messages":false,"can_send_media_messages":false,"can_send_polls":false,"can_send_other_messages":false,"can_add_web_page_previews":false,"can_change_info":false,"can_invite_users":false,"can_pin_messages":false}'
    get_url(url)
    time.sleep(21600)
    delete()

def apne():
    url = URL + 'setChatPermissions?chat_id='+str(chat_id)+'&permissions={"can_send_messages":true,"can_send_media_messages":true,"can_send_polls":true,"can_send_other_messages":true,"can_add_web_page_previews":false,"can_change_info":false,"can_invite_users":false,"can_pin_messages":true}'
    get_url(url)
    time.sleep(25200)
    lock()

def delete():
    ohkk = get_updates()
    for i in range(len(ohkk["result"])):
        cid = ohkk["result"][i]["message"]["chat"]["id"]
        mid = ohkk["result"][i]["message"]["message_id"]
        url = URL + 'deleteMessage?chat_id={}&message_id={}'.format(cid, mid)
        get_url(url)
    time.sleep(39600)
    apne()

def ad_d(message):
    url = URL + 'unpinChatMessage?chat_id='+str(chat_id)
    get_url(url)
    url = URL + 'editMessageText?chat_id='+str(chat_id)+'&message_id=10&text="*update*\n\nThe following courses can accept their admission\n\n\nMedicine and Surgery\nCell Biology and Genetics\nPharmacology\nRadiography\nPhysiotherapy\nPhysiology\nFrench\nComputer Science\nAccounting\nCreative Arts\nBiochemistry\nBusiness Administration\nEducation & Mathematics\nPhysiotherapy\nPolitical science\nArchitecture\nSociology\nEnglish\nInsurance\nEconomics\nMass Communication\nEarly Childhood Education\nHss\nIrpm\nPsychology\nPharmacy\nGeophysics\nElectrical Engineering\nComputer Engineering\nChemical Engineering\nCivil Engineering\nGeology\nBio Medical Engineering\nMedical Lab Science\nSystems Engineering\nMech Engineering\n\n@folami_bot Reporting for Solomoncares"'
    get_url(url)
    url = URL + 'pinChatMessage?chat_id='+str(chat_id)+'&message_id=10'
    get_url(url)

def send_message(message):
    url = URL + 'sendMessage?chat_id='+str(chat_id)+'&text='+message+'...'
    get_url(url)

if __name__ == "__main__":
    while True:
        lock()
