import * as ts from 'typescript';
import * as fs from 'mz/fs';
import * as path from 'path';
import * as _ from 'lodash';
import {
  exec,
} from 'mz/child_process';

export const PLUGIN_ROOT = path.join(__dirname, '../')

export const PROJECT_ROOT = path.join(PLUGIN_ROOT, '../../..')

async function getAST(filename): Promise<ts.SourceFile> {
  const fileContent = await fs.readFile(filename);
  return ts.createSourceFile(
    'same_filename_for_AST_comparison.d.ts',
    fileContent.toString(),
    ts.ScriptTarget.ES2015
  );
}

export async function getGeneratedAST(name: string) {
  return getAST(path.join(__dirname, 'ts_generated', `${name}.d.ts`))
}

export async function getFixtureAST(name: string) {
  return getAST(path.join(__dirname, 'ts_fixtures', `${name}.d.ts`))
}

export async function prepare() {
  await exec('python -m py_codegen.plugins.typescript.__tests__.generate_ts_definitions', {
    cwd: PROJECT_ROOT,
  })
}

export async function clean() {
  await exec('npm run clean', {
    cwd: PLUGIN_ROOT,
  })
}

// prepare()
// clean()