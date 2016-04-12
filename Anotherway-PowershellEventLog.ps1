	
## Another way, if we just know the EntryType of Error , we can change the Event log a little and can repeat the same process.

function Get-VirusEvent 
{ 
    $ErrorLog = Get-EventLog Application -EntryType Error -After (Get-Date).AddDays(-1); 
         
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