import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) {
		int value = 0;
		char variable = '0';
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			String line = br.readLine();
			while(line != null) {
				if (line.indexOf("=") >= 0) {
					variable = line.charAt(0);
					value = line.charAt(2)-'0';
				} else if (line.charAt(0) == variable) {
					System.out.println(value);
				}
				line = br.readLine();
			}
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
		}
	}
}
