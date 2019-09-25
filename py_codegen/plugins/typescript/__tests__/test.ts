import {
  getFixtureAST,
  getGeneratedAST,
  clean,
  prepare,
} from './utils';

export function runTest(name: string) {
  test(`Pycodegen test for ${name}`, async () => {
    const src1 = await getGeneratedAST(name)
    const src2 = await getFixtureAST(name)
    expect(src1).toEqual(src2)
  })
}

function runTests() {
  runTest('ClassWithUnionField');
  runTest('func_with_dict');
  runTest('func_with_list');
  runTest('func_with_typed_dict');
  runTest('func_not_annotated');
  runTest('func_return_none');
  runTest('func_with_tuple');
  runTest('func_with_literals')
}

describe('pycodegen::typescript should...', () => {
  beforeAll(async () => {
    try {
      await clean()
    } catch {

    }
    await prepare()
  })
  runTests()
})
