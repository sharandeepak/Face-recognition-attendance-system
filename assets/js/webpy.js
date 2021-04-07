function create_dataset(){
    var uin = document.getElementById('uid').value
    var fname = document.getElementById('full_name').value
    eel.capture_dataset(uin,fname)(function(ret){console.log(ret)})
}

function train_dataset(){
    toggleloading();
    eel.train_dataset()(function(checkk){if(checkk==3){
            console.log("done");
            toggleloading();
        }})
}
function take_attendance(){
    eel.take_attendance();
}
function open_workbook(){
    eel.open_workbook2();
}
function manual_entry(){
    var uin = document.getElementById('uid2').value; 
    eel.Manual_Entry(uin);
}
function checkPassword(){
    var pass = document.getElementById('passkey').value; 
    if(pass=="123")
    {
        togglePopup3();
    }
    else{
        togglePopup6();
    }
}
function SaveAttendance(){
    toggleloading();
    eel.Save_Attendance()(function(checkk){if(checkk==3){
            console.log("done");
            toggleloading();
        }})
}   