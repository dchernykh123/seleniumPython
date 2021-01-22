#1
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

#2
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

#3
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

#4
assert "login" in browser.current_url, # сообщение об ошибке

#5
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
