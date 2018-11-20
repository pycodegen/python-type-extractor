import { spawn } from 'child_process'

export function runPython(srcFile: string) {
  return new Promise(function (success, nosuccess) {

    const pyprog = spawn('python', [srcFile]);
    let dataCombined: any;
    pyprog.stdout.on('data', function (data) {
      dataCombined = dataCombined += data;
    });
    pyprog.stdout.once('close', function () {
      success(dataCombined);
    })

    pyprog.stderr.on('data', (data) => {

      nosuccess(data);
    });
  })
}