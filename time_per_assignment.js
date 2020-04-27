// A script that determines the average assignment processing time based on the
// rebalancer agent log file entries.

var fs = require('fs');

var args = process.argv.slice(2);
var buf = '';

function main() {
    let assignments = {};
    let difference_sum = 0;
    let count = 0;
    let stream = fs.createReadStream(args[0], {flags: 'r', encoding: 'utf-8'});

    stream.on('data', function(d) {
        buf += d.toString(); // add to global buffer
        processData();
    });

    stream.on('end', function() {
        let mean = difference_sum / count;
        console.log("Average Assignment Download Time: ", mean/1000, "s");
    });

    function processData() {
        let eol;
        
        // Find the end of the line, and keep going as long as we find new
        // lines.
        while ((eol = buf.indexOf('\n')) >= 0) {

            // Send a single line to the line processor
            processLine(buf.slice(0, eol));

            // Set the next character in the buffer to the first character in
            // the next line.
            buf = buf.slice(eol + 1);
        }
    }

    function processLine(line) {
        let obj = JSON.parse(line);

        if (obj.msg.indexOf("Begin processing assignment") !== -1) {
            let assignment_id = obj.msg.split(' ')[4]; 
            assignment_id = assignment_id.replace(".", "");

            assignments[assignment_id] = Date.parse(obj.time);
        }

        if (obj.msg.indexOf("Finished processing assignment") != -1) {
            let assignment_id = obj.msg.split(' ')[4]; 
            assignment_id = assignment_id.replace(".", "");

            if (assignments[assignment_id]  !== undefined) {
                let difference = Date.parse(obj.time) - assignments[assignment_id];
                difference_sum += difference;
                count += 1;
            }
        }
    }
}

main();
