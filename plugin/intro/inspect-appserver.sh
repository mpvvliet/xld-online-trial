#!/bin/sh

encode()
{
    local  myresult=$(printf "%b" "$1" | perl -pe's/([^-_.~A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg')
    echo "$myresult"
}

echo "---"
echo "Inspecting app server '${container.name}'..."
echo "Done."
