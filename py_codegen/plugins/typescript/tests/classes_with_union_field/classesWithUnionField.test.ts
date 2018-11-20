import * as fse from 'fs-extra'
import * as path from 'path'
import * as ts from 'typescript'

import { runPython } from "../runPython";

describe('classes with union field', () => {
  beforeAll(async () => {
    await runPython(path.join(__dirname, 'run.py'))
  })
  it('should test', async () => {
    // const generatedFile = await fse.readFile('generated.ts')
    // const generatedSrcFile = ts.createSourceFile(
    //   'generated.ts',
    //   generatedFile.toString(),
    //   ts.ScriptTarget.ES2015,
    // )
    const program = ts.createProgram(['generated.ts'], {})
    const checker = program.getTypeChecker()
    checker.runWithCancellationToken
  })
})