package de.gdg.devfest.ka.app.calendar;

import de.gdg.devfest.ka.ISetup;
import android.annotation.TargetApi;
import android.os.Build;


/**
 * Background {@link android.app.Service} that adds or removes session Calendar
 * events through the {@link CalendarContract} API available in Android 4.0 or
 * above.
 */
@TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH)
public class SessionCalendarService extends
		com.google.android.apps.iosched.calendar.SessionCalendarService {
	public static final String ACTION_ADD_SESSION_CALENDAR = ISetup.EVENT_PACKAGE_NAME
			+ ".action.ADD_SESSION_CALENDAR";
	public static final String ACTION_REMOVE_SESSION_CALENDAR = ISetup.EVENT_PACKAGE_NAME
			+ ".action.REMOVE_SESSION_CALENDAR";
	public static final String ACTION_UPDATE_ALL_SESSIONS_CALENDAR = ISetup.EVENT_PACKAGE_NAME
			+ ".action.UPDATE_ALL_SESSIONS_CALENDAR";
	public static final String ACTION_UPDATE_ALL_SESSIONS_CALENDAR_COMPLETED = ISetup.EVENT_PACKAGE_NAME
			+ ".action.UPDATE_CALENDAR_COMPLETED";
	public static final String ACTION_CLEAR_ALL_SESSIONS_CALENDAR = ISetup.EVENT_PACKAGE_NAME
			+ ".action.CLEAR_ALL_SESSIONS_CALENDAR";
	public static final String EXTRA_ACCOUNT_NAME = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.ACCOUNT_NAME";
	public static final String EXTRA_SESSION_BLOCK_START = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_BLOCK_START";
	public static final String EXTRA_SESSION_BLOCK_END = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_BLOCK_END";
	public static final String EXTRA_SESSION_TITLE = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_TITLE";
	public static final String EXTRA_SESSION_ROOM = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_ROOM";

}