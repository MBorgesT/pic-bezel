
export class MainPage {

    constructor() {
        this.startPage();
    }

    startPage() {
        document.getElementById("submitButton").onclick = () => this.formAction();
    }

    formAction() {
        var file = document.getElementById('file').files[0];
        var fd = new FormData();
        fd.append('image', file);

        var req = fetch('http://localhost:5000/bezel', {
            method: 'post',
            body: fd
        });

        req.then(function (response) {
            response.blob()
                .then(blob => {
                    var file = window.URL.createObjectURL(blob);
                    window.location.assign(file);
                });
            console.log('success?');
        }, function (error) {
            console.error('failed due to network error or cross domain')
        })
    }

}


function main() {
    new MainPage();
}


window.onload = () => main();

/*
console.log('javascript loaded')

function formAction() {
    console.log('testing');
    var file = document.getElementById('fileForm').datafile;
    var fd = new FormData();
    fd.append('image', file);

    var req = jQuery.ajax({
        url: 'localhost:5000/upload',
        method: 'POST',
        data: fd, // sends fields with filename mimetype etc
        // data: aFiles[0], // optional just sends the binary
        processData: false, // don't let jquery process the data
        contentType: false // let xhr set the content type
    });
}
*/