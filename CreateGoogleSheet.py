import gspread
import urllib.request
from oauth2client.service_account import ServiceAccountCredentials
import argparse
from cligui import cligui


def main():

    parser = argparse.ArgumentParser()

    #EXAMPLE USAGE:
    #python3 CreateGoogleSheet.py -name my-project -email https://docs.google.com/spreadsheets/d/my_google_sheet_url_here
    parser.add_argument("-name", "--sheetname", dest = "name", default = "", help="The name you want for the Google Sheet.  For example: My_Test_Spreadsheet")
    parser.add_argument("-email", "--email", dest = "email", default = "", help="The Email which will get ownership of the Google Sheet. For example: myemail@gmail.com")

    args = parser.parse_args()
    print(args)

    if(args.name!='' and args.sheetsURL!=''):
        processGSpread(args)
    else:
        cligui.CliGui(parser, processGSpread)


def processGSpread(args):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    gc = gspread.authorize(credentials)

    if(args.name!=''):
        userInput = args.name
    else:
        userInput = input("Enter the name you want for the Google Sheet.  For example: My_Test_Spreadsheet\n")
    title = str(userInput)
    #sanitize

    sh = gc.create(title)

    if(args.email!=''):
        userInput = args.email
    else:
        userInput = input("Enter the email to share the Google Sheet to.  For example: myemail@gmail.com\n")
    myEmail = str(userInput)
    #sanitize

    sh.share(myEmail, perm_type='user', role='owner')
    #role – (optional) The primary role for this user. Allowed values are: owner, writer, reader

if __name__ == '__main__':
    main()




# import gspread
#
# gc = gspread.authorize(credentials)
#
# # Open a worksheet from spreadsheet with one shot
# wks = gc.open("Where is the money Lebowski?").sheet1
#
# wks.update_acell('B2', "update b2 with this info.")
#
# # Fetch a cell range
# cell_list = wks.range('A1:B7')

#

#
# from BeautifulSoup import BeautifulSoup as Soup
# import urllib
# import csv
#
# writer = csv.writer(open('ranking.csv','wb'))
# writer.writerow(['RANK', 'NAME','TOTAL_POWERS'])
#
# scores = {}
#
# with open('eeMapSheets.csv','rb') as myfile:
#     csv = myfile.readlines()
#     for row in csv:
#         row = row.split(',')
#         tally = 0
#         for i in range(1,7):
#             try:
#                 row[i] = row[i].strip('\r\n')
#                 tally += eval(row[i])
#             except:
#                 tally =None
#         if (tally != None):
#             scores[tally] = row[0]
# print scores
#
# keylist = scores.keys()
# keylist.sort()
#
# s = 1
# for l in reversed(keylist):
#     writer.writerow([s, scores[l], l])
#     s+=1
