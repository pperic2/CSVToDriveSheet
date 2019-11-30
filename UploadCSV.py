import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main(csvName, URL):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    print(URL)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('ee_test_credentials.json', scope)

    gc = gspread.authorize(credentials)

    print('Authorized...')
    # Read CSV file contents
    #content = open('form-1__tree-inventory.csv', 'r').read()
    content = open(csvName, 'r').read()

    sheetURL = URL

    if(sheetURL == ''):
        #sheetURL = 'https://docs.google.com/spreadsheets/d/1xyqWo7q6nlExkjVAvbrEI8yw0jNeGn3i9VWGUoZU3vw/edit#gid=0'
        userInput = input('Enter a google sheets URL that the bot has access to.  For example: https://docs.google.com/spreadsheets/d/1xyqWo7q6nlExkjVAvbrEI8yw0jNeGn3i9VWGUoZU3vw/edit#gid=0 \n')
        sheetURL = str(userInput)


    print('Uploading to: ' + sheetURL)
    currentSheet = gc.open_by_url(sheetURL)

    gc.import_csv(currentSheet.id, content)

    print('')
    print('Upload completed!')
    print('')


if __name__ == '__main__':
    main(csvName, URL)
