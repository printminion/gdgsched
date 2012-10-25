package de.gdg.devfest.ka;

public interface ISetup {

	public static String EVENT_PACKAGE_NAME = "de.gdg.devfest.ka"; // "com.google.android.apps.iosched"

	/*
	 * Define Activities listed in Manifest + called via Intents
	 */

	public static final Class<?> HomeActivityClass = de.gdg.devfest.ka.app.ui.HomeActivity.class;
	public static final Class<?> AccountActivityClass = de.gdg.devfest.ka.app.ui.AccountActivity.class;
	public static final Class<?> SessionAlarmServiceClass = de.gdg.devfest.ka.app.calendar.SessionAlarmService.class;
	public static final Class<?> ScheduleUpdaterServiceClass = de.gdg.devfest.ka.app.sync.ScheduleUpdaterService.class;
	public static final Class<?> SocialStreamActivityClass = de.gdg.devfest.ka.app.ui.SocialStreamActivity.class;
	public static final Class<?> BeamActivityClass = de.gdg.devfest.ka.app.ui.BeamActivity.class;
	public static final Class<?> MapActivityClass = de.gdg.devfest.ka.app.ui.phone.MapActivity.class;
	public static final Class<?> SessionDetailActivityClass = de.gdg.devfest.ka.app.ui.phone.SessionDetailActivity.class;
	public static final Class<?> SessionsActivityClass = de.gdg.devfest.ka.app.ui.phone.SessionsActivity.class;
	public static final Class<?> TrackDetailActivityClass = de.gdg.devfest.ka.app.ui.phone.TrackDetailActivity.class;
	public static final Class<?> VendorDetailActivityClass = de.gdg.devfest.ka.app.ui.phone.VendorDetailActivity.class;
}
