# sudoku

Web app that assists in solving Sudoku, to practise AWS, React and Python.

* [High level proposal and motivation doc](https://docs.google.com/document/d/1uwK4a110L5XhO8fFHN-IvcFInDLjGKM6XZQFFKP5KME/edit) -
  publicly viewable Google doc.

## Dev notes

#### Backend

1. Setup env:

```powershell
scripts/setup.ps1
```

2. Run the backend server locally:

```powershell
venv\Scripts\activate
python backend\src\handlers\board_parse.py
```

3. Send a request to the local server:

```powershell
$headers = @{
  "Content-Type" = "application/json"
}
$jsonData = @"
{
    "num_columns": 9,
    "num_rows": 9,
    "board_as_text": ""
}
"@
curl -Uri http://127.0.0.1:5000/sudoku/board_parse -Method POST -Headers $headers -Body $jsonData
```
