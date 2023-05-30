import openpyxl
import openai
openai.organization = "org-GmVj8l2x5Oe8yLYMN6MdQG3e"
openai.api_key = "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"
input_file = './data/data.xlsx'
workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active
for row in sheet.iter_rows():
    for cell in row:
        if cell.value:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": ("translate this japanese to vietnamese: " + cell.value ),},
                ]
            )
            modified_content = response['choices'][0]['message']['content']
            cell.value = modified_content
output_file = 'output.xlsx'
workbook.save(output_file)