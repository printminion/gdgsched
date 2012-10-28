package de.gdg.devfest.ka;

import java.util.TimeZone;

import android.annotation.TargetApi;
import android.os.Build;

import com.google.android.apps.iosched.util.ParserUtils;

public class Setup implements ISetup {

	public static String CONFERENCE_HASHTAG = "#devfest";

	public static TimeZone CONFERENCE_TIME_ZONE = TimeZone.getTimeZone("Europe/Berlin");
	
	public static long CONFERENCE_START_MILLIS = ParserUtils.parseTime("2012-11-03T08:30:00.000+01:00");
	public static long CONFERENCE_END_MILLIS = ParserUtils.parseTime("2012-11-03T18:00:00.000+01:00");

	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getMyScheduleWidgetServiceClass() {
		return de.gdg.devfest.ka.app.appwidget.MyScheduleWidgetService.class;
	}
	
	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getMyScheduleWidgetProviderClass() {
		return de.gdg.devfest.ka.app.appwidget.MyScheduleWidgetProvider.class;
	}
	
	@TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH)
	public static final Class<?> getSessionCalendarServiceClass() {
		return de.gdg.devfest.ka.app.calendar.SessionCalendarService.class;
	}

	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getGoogleTVSessionLivestreamActivityClass() {
		return de.gdg.devfest.ka.app.ui.gtv.GoogleTVSessionLivestreamActivity.class;
	}
	
	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getSessionLivestreamActivityClass() {
		return de.gdg.devfest.ka.app.ui.SessionLivestreamActivity.class;
	}
	
	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getMapMultiPaneActivityClass() {
		return de.gdg.devfest.ka.app.ui.tablet.MapMultiPaneActivity.class;
	}
	
	@TargetApi(Build.VERSION_CODES.HONEYCOMB)
	public static final Class<?> getSessionsVendorsMultiPaneActivityClass() {
		return de.gdg.devfest.ka.app.ui.tablet.SessionsVendorsMultiPaneActivity.class;
	}
	
}
