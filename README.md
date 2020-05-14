# Gpu usage alert slack bot(client)
## INSTALL  
 1. install gpu usage alert slack bot(server)
 2. set URL and GPU_ID 
 2. run:    pip install requirements.txt
 3. add to cron
## NAME   
    /remind_gpu -- set alert for gpu memory
## SYNOPSIS
    /remind_gpu [OPTIONS]
    /remind_gpu [gpu_id] [MEMORY_LIST]
## DESCRIPTION
Alerts user when gpu_ids memory usage get lower than MEMORY_LIST
    
    ls
        prints the correspondence between gpu_id:hostname
    help
        prints this message
## EXAMPLE
    /remind_gpu 0 500,500
        When gpu_id=0s first gpu memory usage gets lower than 500MiB and 
        second gpu memory usage gets lower than 500MiB the alert will be sent

