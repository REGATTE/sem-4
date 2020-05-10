package JUnitTestingPackage;

import static org.junit.Assert.*;

import org.junit.Test;

public class testAddStrings {

	@Test
	public void test() {
		
		JUnitFunction jufStrings = new JUnitFunction();
		String result = jufStrings.addStrings("Hello","World");
		assertEquals("HelloWorld",result);
		
	}

}
