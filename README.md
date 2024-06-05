# sudoku

Web app that assists in solving Sudoku, to practise AWS, React and Python.

* [High level proposal and motivation doc](https://docs.google.com/document/d/1uwK4a110L5XhO8fFHN-IvcFInDLjGKM6XZQFFKP5KME/edit) -
  publicly viewable Google doc.

## Dev notes

#### Backend

0. Prerequisite

```powershell
# Enable to run unsigned script in the current process.
Set-ExecutionPolicy Unrestricted -Scope Process
```

1. Setup env:

```powershell
scripts/setup-local.ps1
```

2. Run the backend server locally:

```powershell
venv\Scripts\activate
python backend\server_main.py
deactivate
```

3. Send a request to the local server:

```powershell
$headers = @{
  "Content-Type" = "application/json"
}
$body = @"
{
    "num_columns": 9,
    "num_rows": 9,
    "board_as_text": ""
}
"@
$uri = "http://127.0.0.1:5000/sudoku/board_parse"
curl -Uri $uri -Method POST -Headers $headers -Body $body
```
