export $(cat .env)

mkdir -p "$1"

if !(test -f "$1/$1.py"); then
  cp template.py "$1/$1.py"
fi

curl "https://adventofcode.com/2022/day/$1/input" -X GET -H "Cookie: session=$SESSION_ID" --output "$1/input.txt"
