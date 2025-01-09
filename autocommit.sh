#!/bin/bash

declare -A schedule

# Monday (LUNS)
schedule["16:00-16:50"]="BRS"
schedule["16:50-17:40"]="BRS"
schedule["17:40-18:30"]="PPS"
schedule["18:30-19:20"]="PPS"
schedule["19:20-20:10"]="PPS"
schedule["20:10-21:00"]="AFI"
schedule["21:00-21:50"]="AFI"

# Tuesday (MARTES)
schedule["16:00-16:50"]="NC"
schedule["16:50-17:40"]="NC"
schedule["17:40-18:30"]="NC"
schedule["18:30-19:20"]="HE"
schedule["19:20-20:10"]="HE"
schedule["20:10-21:00"]="HE"
schedule["21:00-21:50"]="ICS"

# Wednesday (MÉRCORES)
schedule["16:00-16:50"]="BRS"
schedule["16:50-17:40"]="BRS"
schedule["17:40-18:30"]="PPS"
schedule["18:30-19:20"]="PPS"
schedule["19:20-20:10"]="ICS"
schedule["20:10-21:00"]="ICS"
schedule["21:00-21:50"]="ICS"

# Thursday (XOVES)
schedule["17:40-18:30"]="HE"
schedule["18:30-19:20"]="HE"
schedule["19:20-20:10"]="AFI"
schedule["20:10-21:00"]="AFI"
schedule["21:00-21:50"]="AFI"

# Friday (VENRES)
schedule["16:00-16:50"]="BRS"
schedule["16:50-17:40"]="BRS"
schedule["17:40-18:30"]="PPS"
schedule["18:30-19:20"]="PPS"
schedule["19:20-20:10"]="ICS"
schedule["20:10-21:00"]="AFI"
schedule["21:00-21:50"]="AFI"

# Get the current time in hours and minutes
current_hour=$(date +"%H")
current_minute=$(date +"%M")

# Convert current time to minutes since midnight
current_time_minutes=$(( current_hour * 60 + current_minute ))

# Loop through the schedule and check if the current time is within any range
found=false
for time_range in "${!schedule[@]}"; do
    # Split the time range into start and end times
    IFS='-' read -r start_time end_time <<< "$time_range"
    
    # Convert start and end times to minutes since midnight
    start_hour=$(echo $start_time | awk -F: '{print $1}')
    start_minute=$(echo $start_time | awk -F: '{print $2}')
    end_hour=$(echo $end_time | awk -F: '{print $1}')
    end_minute=$(echo $end_time | awk -F: '{print $2}')
    
    start_minutes=$(( start_hour * 60 + start_minute ))
    end_minutes=$(( end_hour * 60 + end_minute ))

    # Check if the current time is within the range
    if (( current_time_minutes >= start_minutes && current_time_minutes < end_minutes )); then
        subject="${schedule[$time_range]}"
        echo "Found subject: $subject for current time: $(date +"%H:%M")"
        found=true
        break
    fi
done

# If no subject was found
if [ "$found" = false ]; then
    echo "No subject found for current time: $(date +"%H:%M")"
else
    # Add new files to git
    git add .
    # Commit with the subject abbreviation as the commit message
    git commit -m "$subject"
    # Push the changes
    git push
fi
