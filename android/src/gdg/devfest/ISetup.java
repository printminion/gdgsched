package gdg.devfest;

import android.annotation.TargetApi;
import android.os.Build;


public interface ISetup {

	public static String EVENT_PACKAGE_NAME = "gdg.devfest.app"; // "com.google.android.apps.iosched"

	/*
	 * Define Activities listed in Manifest + called via Intents
	 */

	public static final Class<?> HomeActivityClass = gdg.devfest.app.ui.HomeActivity.class;
	public static final Class<?> AccountActivityClass = gdg.devfest.app.ui.AccountActivity.class;
	public static final Class<?> SessionAlarmServiceClass = gdg.devfest.app.calendar.SessionAlarmService.class;
	public static final Class<?> ScheduleUpdaterServiceClass = gdg.devfest.app.sync.ScheduleUpdaterService.class;
	public static final Class<?> SocialStreamActivityClass = gdg.devfest.app.ui.SocialStreamActivity.class;
	public static final Class<?> BeamActivityClass = gdg.devfest.app.ui.BeamActivity.class;
	public static final Class<?> MapActivityClass = gdg.devfest.app.ui.phone.MapActivity.class;
	public static final Class<?> SessionDetailActivityClass = gdg.devfest.app.ui.phone.SessionDetailActivity.class;
	public static final Class<?> SessionsActivityClass = gdg.devfest.app.ui.phone.SessionsActivity.class;
	public static final Class<?> TrackDetailActivityClass = gdg.devfest.app.ui.phone.TrackDetailActivity.class;
	public static final Class<?> VendorDetailActivityClass = gdg.devfest.app.ui.phone.VendorDetailActivity.class;
	
}
