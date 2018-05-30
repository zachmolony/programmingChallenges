#-------------------------------------------------------------------------------
#   r/dailyprogrammer Challenge #321
#   Talking Clock
#   Desc: A talking clock takes a 24-hour time and translates it into words.
#-------------------------------------------------------------------------------

hr2word = {'00': 'twelve', '01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six', '07': 'seven',
    '08': 'eight', '09': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'one', '14': 'two', '15': 'three',
    '16': 'four', '17': 'five', '18': 'six', '19': 'seven', '20': 'eight', '21': 'nine', '22': 'ten', '23': 'eleven'}

mn2word = {'00': '', '0': 'oh ', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
    '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty ', '30': 'thirty ',
    '40': 'fourty ', '50': 'fifty '}

inp = str(input("Enter the time in xx:xx "))

hr = inp.split(":")[0]
mn = inp.split(":")[1]
mnn = ""
mm = "pm"
try:
    mnn = mn2word[mn]
except:
    if mn[0] == "0":
        mnn = str(mn2word["0"])
    elif mn[0] == "2":
        mnn = str(mn2word["20"])
    elif mn[0] == "3":
        mnn = str(mn2word["30"])
    elif mn[0] == "4":
        mnn = str(mn2word["40"])
    elif mn[0] == "5":
        mnn = str(mn2word["50"])
    if int(hr) < 12:
        mm = "am"
    mnn += mn2word[mn[1]]

print("its", hr2word[hr], mnn, mm)