package gdg.devfest;


public interface ISetup {

	public static String EVENT_PACKAGE_NAME = "gdg.devfest.app"; // "com.google.android.apps.iosched"

	/*
	 * Define Activities listed in Manifest + called vie Intents
	 */

	public static final Class<?> HomeActivityClass = gdg.devfest.app.ui.HomeActivity.class;

	public static final Class<?> AccountActivityClass = gdg.devfest.app.ui.AccountActivity.class;

	public static final Class<?> MyScheduleWidgetServiceClass = gdg.devfest.app.appwidget.MyScheduleWidgetService.class;
	public static final Class<?> MyScheduleWidgetProviderClass = gdg.devfest.app.appwidget.MyScheduleWidgetProvider.class;

	public static final Class<?> SessionLivestreamActivityClass = gdg.devfest.app.ui.SessionLivestreamActivity.class;
	public static final Class<?> SessionAlarmServiceClass = gdg.devfest.app.calendar.SessionAlarmService.class;
	public static final Class<?> SessionCalendarServiceClass = gdg.devfest.app.calendar.SessionCalendarService.class;

	public static final Class<?> ScheduleUpdaterServiceClass = gdg.devfest.app.sync.ScheduleUpdaterService.class;
	public static final Class<?> SocialStreamActivityClass = gdg.devfest.app.ui.SocialStreamActivity.class;

	public static final Class<?> GoogleTVSessionLivestreamActivityClass = gdg.devfest.app.ui.gtv.GoogleTVSessionLivestreamActivity.class;

	public static final Class<?> BeamActivityClass = gdg.devfest.app.ui.BeamActivity.class;

	public static final Class<?> MapActivityClass = gdg.devfest.app.ui.phone.MapActivity.class;
	public static final Class<?> SessionDetailActivityClass = gdg.devfest.app.ui.phone.SessionDetailActivity.class;
	public static final Class<?> SessionsActivityClass = gdg.devfest.app.ui.phone.SessionsActivity.class;
	public static final Class<?> TrackDetailActivityClass = gdg.devfest.app.ui.phone.TrackDetailActivity.class;
	public static final Class<?> VendorDetailActivityClass = gdg.devfest.app.ui.phone.VendorDetailActivity.class;

	public static final Class<?> MapMultiPaneActivityClass = gdg.devfest.app.ui.tablet.MapMultiPaneActivity.class;
	public static final Class<?> SessionsVendorsMultiPaneActivityClass = gdg.devfest.app.ui.tablet.SessionsVendorsMultiPaneActivity.class;

	
}
