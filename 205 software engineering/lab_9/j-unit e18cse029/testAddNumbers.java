package JUnitTestingPackage;

import static org.junit.Assert.*;

import org.junit.Test;

public class testAddNumbers {

	@Test
	public void test() {
		
		JUnitFunction jufNumbers = new JUnitFunction();
		int result = jufNumbers.addNumbers(100,200);
		assertEquals(300,result);
		
	}

}
