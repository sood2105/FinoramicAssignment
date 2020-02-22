echo "Enter complete filename"
read filename
# cat ${filename} | sed 's/[{}, ]//g' > temp.txt
cat ${filename} | sed -e '/{$/d' -e '/^}/d' -e 's/,//' | sort | grep -v -e "^pip" -e "^setuptools" > temp_requirments.txt
pip install -r temp_requirments.txt
pip freeze > installed_dependencies.txt
comm -23 temp_requirments.txt installed_dependencies.txt > dependencies_not_installed.txt
if [ ! -s dependencies_not_installed.txt ]; 
then
	echo -e "\nAll dependencies successfully installed\n"
else 
	echo -e "\nFollowing dependencies are not installed:"
	cat dependencies_not_installed.txt
fi
rm -f dependencies_not_installed.txt temp_requirments.txt installed_dependencies.txt

