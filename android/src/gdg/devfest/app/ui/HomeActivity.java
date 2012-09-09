package gdg.devfest.app.ui;

/**
 * The landing screen for the app, once the user has logged in.
 * 
 * <p>
 * This activity uses different layouts to present its various fragments,
 * depending on the device configuration. {@link MyScheduleFragment},
 * {@link ExploreFragment}, and {@link SocialStreamFragment} are always
 * available to the user. {@link WhatsOnFragment} is always available on tablets
 * and phones in portrait, but is hidden on phones held in landscape.
 * 
 * <p>
 * On phone-size screens, the three fragments are represented by
 * {@link ActionBar} tabs, and can are held inside a {@link ViewPager} to allow
 * horizontal swiping.
 * 
 * <p>
 * On tablets, the three fragments are always visible and are presented as
 * either three panes (landscape) or a grid (portrait).
 */
public class HomeActivity extends
		com.google.android.apps.iosched.ui.HomeActivity {
}
