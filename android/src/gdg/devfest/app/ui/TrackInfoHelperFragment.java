package gdg.devfest.app.ui;

/**
 * A retained, non-UI helper fragment that loads track information such as name,
 * color, etc. and returns this information via
 * {@link Callbacks#onTrackInfoAvailable(String, String, int)}.
 */
public class TrackInfoHelperFragment extends
		com.google.android.apps.iosched.ui.TrackInfoHelperFragment {

	/**
	 * The track URI for which to load data.
	 */
	public static final String ARG_TRACK = "com.google.android.iosched.extra.TRACK";

}
