package gdg.devfest.ch;

public interface ISetup {

	public static String EVENT_PACKAGE_NAME = "gdg.devfest.ch"; // "com.google.android.apps.iosched"

	/*
	 * Define Activities listed in Manifest + called vie Intents
	 */

	public static final Class<?> HomeActivityClass = gdg.devfest.ch.app.ui.HomeActivity.class;

	public static final Class<?> AccountActivityClass = gdg.devfest.ch.app.ui.AccountActivity.class;

	public static final Class<?> SessionAlarmServiceClass = gdg.devfest.ch.app.calendar.SessionAlarmService.class;

	public static final Class<?> ScheduleUpdaterServiceClass = gdg.devfest.ch.app.sync.ScheduleUpdaterService.class;
	public static final Class<?> SocialStreamActivityClass = gdg.devfest.ch.app.ui.SocialStreamActivity.class;

	public static final Class<?> BeamActivityClass = gdg.devfest.ch.app.ui.BeamActivity.class;

	public static final Class<?> MapActivityClass = gdg.devfest.ch.app.ui.phone.MapActivity.class;
	public static final Class<?> SessionDetailActivityClass = gdg.devfest.ch.app.ui.phone.SessionDetailActivity.class;
	public static final Class<?> SessionsActivityClass = gdg.devfest.ch.app.ui.phone.SessionsActivity.class;
	public static final Class<?> TrackDetailActivityClass = gdg.devfest.ch.app.ui.phone.TrackDetailActivity.class;
	public static final Class<?> VendorDetailActivityClass = gdg.devfest.ch.app.ui.phone.VendorDetailActivity.class;
	
}
