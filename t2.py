from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tables")

def extract_table_data(table_id):
    table = driver.find_element(By.ID, table_id)
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            data.append([cell.text for cell in cells])
    return data

table_data = extract_table_data("table1")

print("Company names:")
for row in table_data:
    print(row[0])

company_to_find = "Jason Doe"
exists = any(f"{row[0]} {row[1]}" == company_to_find for row in table_data)
print(f"\nExists: {exists}")

input("\nPress Enter to close...")
