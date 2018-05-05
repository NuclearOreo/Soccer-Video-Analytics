 for filename in *.jpg;
do
  SUBSTRING=$(echo $filename| cut -d'.' -f 1)
  if !(($SUBSTRING % 20)); then
        echo "Moving file" $filename "to filtered folder"
        cp $filename ../filtered
  fi
done
