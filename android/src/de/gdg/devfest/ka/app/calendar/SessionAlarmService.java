package de.gdg.devfest.ka.app.calendar;

import de.gdg.devfest.ka.ISetup;

/**
 * Background service to handle scheduling of starred session notification via
 * {@link android.app.AlarmManager}.
 */
public class SessionAlarmService extends
		com.google.android.apps.iosched.calendar.SessionAlarmService {

	public static final String ACTION_NOTIFY_SESSION = ISetup.EVENT_PACKAGE_NAME
			+ ".action.NOTIFY_SESSION";
	public static final String ACTION_SCHEDULE_STARRED_BLOCK = ISetup.EVENT_PACKAGE_NAME
			+ ".action.SCHEDULE_STARRED_BLOCK";
	public static final String ACTION_SCHEDULE_ALL_STARRED_BLOCKS = ISetup.EVENT_PACKAGE_NAME
			+ ".action.SCHEDULE_ALL_STARRED_BLOCKS";
	public static final String EXTRA_SESSION_START = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_START";
	public static final String EXTRA_SESSION_END = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_END";
	public static final String EXTRA_SESSION_ALARM_OFFSET = ISetup.EVENT_PACKAGE_NAME
			+ ".extra.SESSION_ALARM_OFFSET";

}
