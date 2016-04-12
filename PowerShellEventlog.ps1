function Get-VirusEvent 
{ 
    $EventLog = Get-EventLog -LogName Application -After(Get-Date).AddDays(-1) | foreach {$_.Source.Trim().ToUpper()} 
         
    $badeventservice = "BONJOUR SERVICE"
    $badeventDefinitions = $badevent -split ","     
 
 
    foreach($badeventservice in $badeventDefinitions) 
    { 
        Write-Host("Checking $badeventservice")        
        if($EventLog.Contains($badeventservice.Trim().ToUpper()))
        { 
            Write-Host("Sorry, you have been infected with $badeventservice")                
        }         
    } 
    Write-Host("Congrats, you are all clean, carry on...") 
}  
