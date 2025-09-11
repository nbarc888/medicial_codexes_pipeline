Where your at with the git session
```
git status
```

Starting a feature:
```
git checkout -b nbarcleon-dev
```

Knowing where you are
```
git log --all --oneline --graph
```

Run Test Script:
```
python scripts\test.py
```



### example imports # Example usage:
### employees = [
 ###    {'name': 'Alice', 'department': 'HR'},
  ###  {'name': 'Bob', 'department': 'Engineering'},
  ###  {'name': 'Charlie', 'department': 'HR'}
###]
###headers = ['name', 'department']
###save_to_csv(employees, 'employees.csv', headers)