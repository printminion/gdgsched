package gdg.devfest;

import java.util.TimeZone;

import com.google.android.apps.iosched.util.ParserUtils;

public class Setup implements ISetup {

	public static String CONFERENCE_HASHTAG = "#devfest";

//	public static TimeZone CONFERENCE_TIME_ZONE = TimeZone
//			.getTimeZone("America/Los_Angeles");

	public static TimeZone CONFERENCE_TIME_ZONE = TimeZone.getTimeZone("Europe/Berlin");
	
	
//	public static TimeZone CONFERENCE_TIME_ZONE = TimeZone
//			.getTimeZone("Europe/Berlin");
//	public static long CONFERENCE_START_MILLIS = ParserUtils
//			.parseTime("2012-06-27T09:30:00.000-07:00");
//
//	public static long CONFERENCE_END_MILLIS = ParserUtils
//			.parseTime("2012-06-29T18:00:00.000-07:00");

	public static long CONFERENCE_START_MILLIS = ParserUtils.parseTime("2012-10-13T09:00:00.000+02:00");
	public static long CONFERENCE_END_MILLIS = ParserUtils.parseTime("2012-10-14T19:00:00.000+02:00");

}
