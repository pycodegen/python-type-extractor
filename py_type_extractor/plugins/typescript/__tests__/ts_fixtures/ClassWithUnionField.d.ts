export class SomeClass {

}

export class ClassWithUnionField {
   	cwufField1: null | undefined
		| number
		| SomeClass;
}