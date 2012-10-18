package gdg.devfest.ch.app.sync;

import gdg.devfest.ch.Setup;

/**
 * Background {@link android.app.Service} that adds or removes sessions from
 * your calendar via the Conference API.
 * 
 * @see com.google.android.apps.iosched.sync.SyncHelper
 */
public class ScheduleUpdaterService extends
		com.google.android.apps.iosched.sync.ScheduleUpdaterService {

	public static final String EXTRA_SESSION_ID = Setup.EVENT_PACKAGE_NAME + ".extra.SESSION_ID";
	public static final String EXTRA_IN_SCHEDULE = Setup.EVENT_PACKAGE_NAME + ".extra.IN_SCHEDULE";

}
