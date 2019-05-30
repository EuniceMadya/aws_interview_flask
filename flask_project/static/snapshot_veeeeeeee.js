var parent = document.getElementById("pending_EC2_info");
var parent_suc = document.getElementById("success_EC2_info");
var dscn = document.createElement('h4');
dscn.innerHTML = "Description";
var snapshotID = document.createElement('h4');
snapshotID.innerHTML = "SnapshotID";
var startTime = document.createElement('h4');
startTime.innerHTML = "start Time"
var state = document.createElement('h4');
state.innerHTML = "State";
var volumeSize = document.createElement('h4');
volumeSize.innerHTML = "volume Size";

var id = "";

parent.appendChild(dscn);
parent.appendChild(snapshotID);
parent.appendChild(startTime);
parent.appendChild(state);
parent.appendChild(volumeSize);




var state_suc = document.createElement('h4');
state_suc.innerHTML = "State";

parent_suc.appendChild(state_suc);

// console.log('{{SECRETE_KEY|tojson }}');




function create_snapShot(keys){

  var ec2 = new AWS.EC2({ accessKeyId: keys.KEY_aws,
  secretAccessKey: keys.secretAccessKey, region: 'ap-southeast-2' });

  console.log("ahh");
  var dscn_c = document.createElement('p');
  var snapshotID_c = document.createElement('p');
  var startTime_c = document.createElement('p');
  var state_c = document.createElement('p');
  var volumeSize_c = document.createElement('p');

  var params = {
    VolumeId: "vol-09fbdf4ec8a0a0695", /* required */
    Description: "This is created for the testing purpose",
    };

    ec2.createSnapshot(params).promise().then(function(data){
          console.log(data.SnapshotId);
          var status = data.State;
          dscn_c.innerHTML = data.Description;
          dscn.appendChild(dscn_c);
          snapshotID_c.innerHTML = data.SnapshotId;
          snapshotID.appendChild(snapshotID_c);
          id =  data.SnapshotId;
          startTime_c.innerHTML = data.StartTime;
          startTime.appendChild(startTime_c);
          state_c.innerHTML = data.State;
          state.appendChild(state_c);
          volumeSize_c.innerHTML = data.VolumeSize;
          volumeSize.appendChild(volumeSize_c);

      return ec2.waitFor('snapshotCompleted', { SnapshotIds: [data.SnapshotId] }).promise();
    }).then(function(data){
      param = {
        SnapshotIds: [
          id
        ]
      }
      // console.log(param.SnapshotIds[0]);

      request = ec2.describeSnapshots(param, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        // else     console.log(data.Snapshots);           // successful response
      });
      request.on('success', function(response) {

        console.log(response.data.Snapshots[0].Description);
        var data = response.data.Snapshots[0];

        var state_c_suc = document.createElement('p');


        state_c_suc.innerHTML = data.State;
        state_suc.appendChild(state_c_suc);

        //encrypted//tag//

});

    });

}

function check_snapShot(){
  param = {

    SnapshotIds: [
      "snap-023a842c7f3f0a57b"
    ]

  }
  request = ec2.describeSnapshots(param, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    // else     console.log(data.Snapshots);           // successful response
  });
  request.on('success', function(response) {  console.log(response.data.Snapshots[0].Description);
    var data = response.data.Snapshots[0];

    var dscn_c_suc = document.createElement('p');
    var snapshotID_c_suc = document.createElement('p');
    var startTime_c_suc = document.createElement('p');
    var state_c_suc = document.createElement('p');
    var volumeSize_c_suc = document.createElement('p');

    dscn_c_suc.innerHTML = data.Description;
    dscn_suc.appendChild(dscn_c_suc);
    snapshotID_c_suc.innerHTML = data.SnapshotId;
    snapshotID_suc.appendChild(snapshotID_c_suc);
    id =  data.SnapshotId;
    startTime_c_suc.innerHTML = data.StartTime;
    startTime_suc.appendChild(startTime_c_suc);
    state_c_suc.innerHTML = data.State;
    state_suc.appendChild(state_c_suc);
    volumeSize_c_suc.innerHTML = data.VolumeSize;
    volumeSize_suc.appendChild(volumeSize_c_suc);





  });

}
