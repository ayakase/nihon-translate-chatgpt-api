import openpyxl
import openai
openai.api_key = "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"
input_file = './data/Spec_JP.xlsx'
workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active
for row in sheet.iter_rows():
    for cell in row:
        if cell.value is not None and isinstance(cell.value, str) and not cell.value.isascii() and '=' not in cell.value:
            print (cell.value)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": ("translate this japanese to english : " + cell.value ),},
                ]
            )
            modified_content = response['choices'][0]['message']['content']
            cell.value = modified_content
        elif isinstance(cell.value, int):
            continue
        elif cell.value is not None and '=' in cell.value:
            cell.value = cell.value
output_file = 'output.xlsx'
workbook.save(output_file)