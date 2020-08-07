export class SomeClass {
   	a: number; 
}
export function func_with_typed_dict(
    	input: INestedTypedDict,
): IOutputType
export interface ISimpleTypedDict1 {
		a: string,
}
export interface INestedTypedDict {
		child: ISimpleTypedDict1,
}
export interface IOutputType {
		b: number,
		'some thing': string,
		s: SomeClass,
}