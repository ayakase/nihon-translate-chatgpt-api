import openpyxl
import openai
openai.api_key = ""
input_file = './data/Testcase_JP.xlsx'
workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active
for row in sheet.iter_rows():
    for cell in row:
        if cell.value:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": ("translate this japanese to vietnamese (if you see special character, english or you cant translate, response exactly what I input): [" + cell.value + "]"),},
                ]
            )
            modified_content = response['choices'][0]['message']['content']
            cell.value = modified_content
output_file = 'output.xlsx'
workbook.save(output_file)